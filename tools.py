# ============================================================================
# 文件名: tools.py
# 功能: 定义研究助手 Agent 可用的工具集
# 说明: Agent 通过这些工具来执行实际操作（搜索、查询、保存数据等）
# ============================================================================

# ============================================================================
# 第1部分: 导入依赖库
# ============================================================================
from langchain_core.tools import Tool, tool      # LangChain 工具类：将普通 Python 函数包装成 Agent 可调用的工具
from datetime import datetime              # Python 标准库：处理日期和时间（用于生成时间戳）
import urllib.request                      # Python 标准库：HTTP 请求（预留使用，当前未用到）
import json                                # Python 标准库：处理 JSON 数据（预留使用，当前未用到）
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

import os
import subprocess
import sys
import io
from contextlib import redirect_stdout, redirect_stderr

# ... existing code ...

# ============================================================================
# 第2部分: 工具函数定义
# ============================================================================

# ----------------------------------------------------------------------------
# 工具1: save_to_txt - 文件保存工具
# 功能: 将研究数据保存到本地文本文件，并自动添加时间戳
# 使用场景: 保存研究成果、日志记录、数据持久化
# ----------------------------------------------------------------------------
def save_to_txt(data: str, filename: str = None):
    """
    将研究数据保存到文本文件（自动使用时间戳生成唯一文件名）
    
    Args:
        data: 要保存的研究数据内容（字符串格式）
        filename: 文件名（可选，如果不提供则自动生成带时间戳的文件名）
                  格式: research_output_2026-04-10_15-30-25.txt
    
    Returns:
        str: 保存成功的确认信息

    """
    # 如果没有提供文件名，则根据当前时间自动生成唯一文件名
    if filename is None:
        # 生成格式：research_output_年-月-日_时-分-秒.txt
        # 例如：research_output_2026-04-10_15-30-25.txt
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"生成文件_{timestamp}.txt"
    
    # 获取当前系统时间，用于文件内容中的时间戳
    timestamp_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 使用 f-string 拼接格式化的文本
    # 结构: 标题 → 时间戳 → 空行 → 数据内容 → 空行
    # 例如:
    # --- Research Output ---
    # Timestamp: 2026-04-10 15:30:25
    #
    # Python 是一种高级编程语言...
    #
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp_content}\n\n{data}\n\n"

    # 以追加模式打开文件并写入数据
    # open(filename, "a", encoding="utf-8"):
    #   - "a" 模式: Append（追加），不会覆盖已有内容，新内容添加到文件末尾
    #   - encoding="utf-8": 支持中文和其他 Unicode 字符，避免乱码
    # with 语句: 上下文管理器，自动在代码块结束后关闭文件（即使发生异常）
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    # 返回确认信息给 Agent，让 Agent 知道文件保存成功
    return f"Data successfully saved to {filename}"


# ----------------------------------------------------------------------------
# 工具2: web_search - 网页搜索工具
# 功能: 使用 DuckDuckGo 搜索引擎查询互联网信息
# 特点: 免费、无需 API Key、隐私保护
# 使用场景: 获取最新的网络信息、新闻、教程等
# ----------------------------------------------------------------------------
def web_search(query: str) -> str:
    """
    使用 DuckDuckGo 搜索网页信息
    
    Args:
        query: 搜索关键词（例如："Python programming"、"人工智能最新进展"）
    
    Returns:
        str: 搜索结果文本，包含标题和摘要（最多3条）
    
    返回格式示例:
        "Python (programming language): Python is a high-level, general-purpose...
        
        Guido van Rossum: Guido van Rossum is a Dutch programmer...
        
        Python Software Foundation: The Python Software Foundation is..."
    
    异常处理:
        如果搜索失败（网络错误、API 限制等），返回错误信息而不是抛出异常
    """
    # 使用 try-except 捕获所有可能的异常
    # 网络请求可能失败：断网、DNS 解析失败、API 限流等
    try:
        # 延迟导入：只在函数执行时才导入模块
        # 优点：
        #   1. 避免启动时就加载所有依赖
        #   2. 如果模块未安装，不影响其他功能
        #   3. 加快模块初始化速度
        from ddgs import DDGS  # DuckDuckGo 搜索的 Python 客户端库
        
        # 使用 with 语句创建搜索客户端
        # DDGS() 初始化搜索引擎客户端
        # with 语句确保使用完毕后自动释放资源（如关闭网络连接）
        with DDGS() as ddgs:
            # 执行文本搜索
            # query: 用户输入的搜索关键词
            # max_results=3: 限制返回结果数量（避免信息过载，节省 token）
            results = ddgs.text(query, max_results=3)
            
            # 检查是否有搜索结果
            if results:
                # 使用列表推导式格式化搜索结果
                # 原始结果格式: [{"title": "...", "body": "...", "href": "..."}, ...]
                # 目标格式: "标题1: 摘要1\n\n标题2: 摘要2\n\n标题3: 摘要3"
                #
                # 列表推导式详解:
                # [f"{r['title']}: {r['body']}" for r in results]
                #   ↓ 等价于 ↓
                # formatted_list = []
                # for r in results:  # 遍历每个搜索结果
                #     formatted_item = f"{r['title']}: {r['body']}"  # 格式化
                #     formatted_list.append(formatted_item)
                #
                # "\n\n".join(...): 用双换行符连接所有结果
                return "\n\n".join([f"{r['title']}: {r['body']}" for r in results])
            
            # 如果没有搜索结果，返回提示信息
            return "No results found"
    
    except Exception as e:
        # 捕获所有异常并返回错误信息
        # str(e): 将异常对象转换为字符串（错误描述）
        # 这样 Agent 能看到错误信息并决定下一步操作
        return f"Search failed: {str(e)}"


# ----------------------------------------------------------------------------
# 工具3: wiki_search - 维基百科搜索工具
# 功能: 从维基百科获取主题的权威摘要信息
# 特点: 内容权威、结构化、适合查询概念和背景知识
# 使用场景: 查询名词解释、历史背景、科学概念等
# ----------------------------------------------------------------------------
def wiki_search(query: str) -> str:
    """
    从维基百科查询信息
    
    Args:
        query: 查询主题（例如："Machine learning"、"Python programming"）
    
    Returns:
        str: 维基百科词条摘要（最多3句话）
    
    返回示例:
        "Python is a high-level, general-purpose programming language. Its design 
        philosophy emphasizes code readability with the use of significant 
        indentation. Python is dynamically typed and garbage-collected."
    
    异常处理:
        如果词条不存在、网络错误或语言不支持，返回错误信息
    """
    # 使用 try-except 处理可能的异常
    try:
        # 延迟导入维基百科 API 客户端
        import wikipedia  # Python 维基百科库
        
        # 设置查询语言为英语
        # wikipedia.set_lang("en"):
        #   - "en": 英语维基百科（内容最全面，1000万+词条）
        #   - 可选值: "zh"（中文）、"ja"（日语）、"fr"（法语）等
        # 为什么选择英语？
        #   1. 技术类词条英文最全面、最准确
        #   2. 大多数学术概念的标准命名是英文
        #   3. 中文维基百科可能缺少某些专业术语
        wikipedia.set_lang("zh")
        
        # 获取词条摘要
        # wikipedia.summary(query, sentences=3):
        #   - query: 查询的词条名称
        #   - sentences=3: 限制返回3句话（避免返回整篇长文，节省 token）
        #   - 返回的是词条第一段的精简版（摘要部分）
        summary = wikipedia.summary(query, sentences=3)
        
        # 返回摘要文本给 Agent
        return summary
    
    except Exception as e:
        # 常见异常：
        #   - DisambiguationError: 词条名不明确，有多个匹配（如 "Python" 可以是编程语言或蟒蛇）
        #   - PageError: 词条不存在
        #   - HTTPError: 网络请求失败
        return f"Wikipedia search failed: {str(e)}"

# ----------------------------------------------------------------------------
# 工具4: exit_agent - 退出程序工具
# 功能: 当用户说再见时，优雅地退出程序
# 注意: 必须接受一个参数（LangChain Tool 调用时会传入参数）
# ----------------------------------------------------------------------------
def exit_agent(_input: str = "") -> str:
    """
    退出 Agent 程序
    
    Args:
        _input: 占位符参数（LangChain Tool 调用时必须传入，但这里不使用）
    
    Returns:
        str: 退出确认信息
    """
    print("\n👋 Goodbye! 感谢使用，再见！")
    exit(0)
    # 返回消息让 Agent 知道已退出（实际上程序会立即终止）


# ----------------------------------------------------------------------------
# 工具5: get_datatime - 获取当前时间工具
# 功能: 返回当前日期和时间
# 注意: 必须接受一个参数（LangChain Tool 调用时会传入参数）
# ----------------------------------------------------------------------------
def get_datetime(_input: str = "") -> str:
    """
    获取当前日期和时间
    
    Args:
        _input: 占位符参数（LangChain Tool 调用时必须传入，但这里不使用）
    
    Returns:
        str: 格式化的当前时间字符串
    """
    # datetime.now() 返回 datetime 对象，需要转换为字符串
    current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    return f"当前时间: {current_time}"


# ----------------------------------------------------------------------------
# 工具6: read_document - 读取 Word 文档工具
# 功能: 读取 .doc 或 .docx 文件的内容
# 使用场景: Agent 需要分析用户上传的 Word 文档时
# ----------------------------------------------------------------------------
def read_document(file_path: str) -> str:
    """
    读取 Word 文档（.doc 或 .docx）的内容

    Args:
        file_path: Word 文档的文件路径（相对路径或绝对路径）

    Returns:
        str: 文档的文本内容

    异常处理:
        如果文件不存在、格式错误或读取失败，返回错误信息
    """
    try:
        if not os.path.exists(file_path):
            return f"错误：文件不存在 - {file_path}"

        if not (file_path.endswith('.doc') or file_path.endswith('.docx')):
            return f"错误：不支持的文件格式，仅支持 .doc 和 .docx 文件"

        loader = UnstructuredWordDocumentLoader(file_path)
        documents = loader.load()

        if not documents:
            return f"错误：文档内容为空 - {file_path}"

        content = "\n\n".join([doc.page_content for doc in documents])

        if len(content) > 10000:
            content = content[:10000] + "\n\n[文档内容较长，已截取前10000字符]"

        return f"文档路径: {file_path}\n文档长度: {len(content)} 字符\n\n--- 文档内容 ---\n{content}"

    except Exception as e:
        return f"读取文档失败: {str(e)}"


# ----------------------------------------------------------------------------
# 工具8: read_python_file - 读取 Python 文件工具
# 功能: 读取 .py 文件的完整内容
# 使用场景: Agent 需要查看和分析 Python 代码时
# ----------------------------------------------------------------------------
@tool
def read_python_file(file_path: str) -> str:
    """
    读取 Python 文件的完整内容
    
    Args:
        file_path: Python 文件的路径（相对或绝对路径）
    
    Returns:
        str: 文件的完整内容，包含行号
    """
    try:
        if not os.path.exists(file_path):
            return f"错误：文件不存在 - {file_path}"
        
        if not file_path.endswith('.py'):
            return f"错误：不是 Python 文件（.py）- {file_path}"
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 添加行号
        numbered_lines = []
        for i, line in enumerate(lines, 1):
            numbered_lines.append(f"{i:4d} | {line.rstrip()}")
        
        content = "\n".join(numbered_lines)
        total_lines = len(lines)
        
        return f"文件: {file_path}\n总行数: {total_lines}\n\n--- 文件内容 ---\n{content}"
    
    except Exception as e:
        return f"读取文件失败: {str(e)}"


# ----------------------------------------------------------------------------
# 工具9: save_python_file - 保存/修改 Python 文件工具
# 功能: 保存修改后的 Python 代码到文件
# 使用场景: Agent 修改代码后保存文件
# ----------------------------------------------------------------------------
@tool
def save_python_file(code: str, file_path: str) -> str:
    """
    保存 Python 代码到文件（覆盖原文件或创建新文件）
    
    Args:
        code: 要保存的 Python 代码内容
        file_path: 保存的文件路径
    
    Returns:
        str: 保存成功的确认信息
    """
    try:
        # 确保目录存在
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # 写入文件（覆盖模式）
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        
        # 计算行数
        lines = code.count('\n') + 1
        
        return f"✅ 文件已成功保存: {file_path}\n📊 代码行数: {lines} 行\n💾 文件大小: {len(code.encode('utf-8'))} 字节"
    
    except Exception as e:
        return f"❌ 保存文件失败: {str(e)}"
# ----------------------------------------------------------------------------
# 工具7: run_python_code - Python 代码执行工具
# 功能: 安全地执行 Python 代码并返回结果
# 使用场景: Agent 需要运行代码示例、计算、数据处理等
# ----------------------------------------------------------------------------
def run_python_code(code: str) -> str:
    """
    执行 Python 代码或运行 Python 文件
    
    Args:
        code: 要执行的 Python 代码字符串，或者是文件路径（如果以 .py 结尾）
    
    Returns:
        str: 代码执行的输出结果或错误信息
    
    支持的功能:
        - 直接执行 Python 代码字符串
        - 运行 .py 文件（传入文件路径）
        - 导入常用安全模块（math, random, json, datetime 等）
    """
    try:
        # 检查是否是文件路径
        if code.strip().endswith('.py'):
            # 尝试读取并执行 Python 文件
            file_path = code.strip()
            if not os.path.exists(file_path):
                return f"错误：文件不存在 - {file_path}"
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
            except Exception as e:
                return f"读取文件失败: {str(e)}"
        
        # 创建执行环境，允许导入安全的模块
        safe_globals = {
            '__builtins__': __builtins__,  # 允许所有内置函数
            '__name__': '__main__',
            '__file__': '<executed_code>',
        }
        
        # 预导入常用的安全模块
        safe_modules = [
            'math', 'random', 'datetime', 'json', 'collections',
            'itertools', 'functools', 're', 'string', 'time',
            'copy', 'decimal', 'fractions', 'statistics',
            'typing', 'dataclasses'
        ]
        
        for module_name in safe_modules:
            try:
                module = __import__(module_name)
                safe_globals[module_name] = module
            except ImportError:
                pass
        
        # 捕获标准输出和错误输出
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()
        
        try:
            # 重定向输出
            with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                # 执行代码
                exec(compile(code, '<code>', 'exec'), safe_globals)
            
            # 获取输出
            stdout = stdout_buffer.getvalue()
            stderr = stderr_buffer.getvalue()
            
            # 组合结果
            result = []
            if stdout:
                result.append("=== 输出结果 ===")
                result.append(stdout.rstrip())
            
            if stderr:
                result.append("=== 错误信息 ===")
                result.append(stderr.rstrip())
            
            if not result:
                return "✅ 代码执行成功，但没有输出"
            
            return "\n\n".join(result)
            
        except Exception as e:
            error_msg = f"❌ 执行错误:\n{type(e).__name__}: {str(e)}"
            # 如果有部分输出，也包含进来
            stdout = stdout_buffer.getvalue()
            if stdout:
                error_msg = f"=== 部分输出 ===\n{stdout}\n\n{error_msg}"
            return error_msg
    
    except Exception as e:
        return f"代码执行失败: {str(e)}"




# ============================================================================
# 第3部分: 工具注册
# ============================================================================
# 将上面定义的函数包装成 LangChain 的 Tool 对象
# Agent 通过 Tool 的 name 和 description 来决定何时调用哪个工具
#
# Tool 类的三个核心参数:
#   - name: 工具名称（唯一标识符，Agent 调用时使用）
#   - func: 实际执行的 Python 函数
#   - description: 工具功能描述（**非常重要**，Agent 根据描述决定是否使用该工具）
# ============================================================================

# ----------------------------------------------------------------------------
# 工具注册 1: save_text_to_file
# 用途: 保存研究数据到本地文件
# 调用时机: Agent 收集完信息后，需要持久化存储时
# ----------------------------------------------------------------------------
save_tool = Tool(
    name="save_text_to_file",    # 工具名称：语义明确，Agent 容易理解
    func=save_to_txt,            # 绑定的函数：上面定义的 save_to_txt
    description="保存搜索结果到本地文件,传入两个参数,第一个为保存内容，第二个为保存的文件名",  # 功能描述：简洁明了
)

# ----------------------------------------------------------------------------
# 工具注册 2: search
# 用途: 搜索互联网获取最新信息
# 调用时机: 用户需要查询新闻、教程、最新资料时
# 描述设计技巧:
#   - 明确搜索源："using DuckDuckGo"（让 Agent 知道搜索引擎）
#   - 提示输入格式："Input: search query string"（指导 Agent 如何传参）
# ----------------------------------------------------------------------------
search_tool = Tool(
    name="search",               # 工具名称：简短有力
    func=web_search,             # 绑定的函数：上面定义的 web_search
    description="Search the web for information using DuckDuckGo. Input: search query string.",
)

# ----------------------------------------------------------------------------
# 工具注册 3: wikipedia
# 用途: 查询权威百科知识
# 调用时机: 用户询问概念定义、背景知识、历史信息等
# 关键词设计:
#   - "encyclopedic": 强调百科全书式的权威信息
#   - "topic or keyword": 提示适合查询主题性知识
# ----------------------------------------------------------------------------
wiki_tool = Tool(
    name="wikipedia",            # 工具名称：直接使用 Wikipedia 这个广为人知的名字
    func=wiki_search,            # 绑定的函数：上面定义的 wiki_search
    description="Search Wikipedia for encyclopedic information. Input: topic or keyword.",
)

exit_tool = Tool(
    name="exit",
    func=exit_agent,
    description="if user say goodbye",
)

time_tool = Tool(
    name="get_time",
    func=get_datetime,
    description="get current time",
)

read_doc_tool = Tool(
    name="read_document",
    func=read_document,
    description="读取Word文档(.doc或.docx)的完整内容。使用方法：传入文件的绝对路径或相对路径。例如：'李健驹论文.docx' 或 'D:/python_ai_agent/mytest/李健驹论文.docx'。此工具会返回文档的全部文本内容，供后续分析和总结使用。",
)

run_code_tool = Tool(
    name="run_python_code",
    func=run_python_code,
    description="执行Python代码或运行.py文件。用法：1) 直接传入代码字符串，如'print(2+2)'；2) 传入.py文件路径，如'test_code_execution.py'。支持导入常用模块(math, random, json, datetime等)。可以执行计算、数据处理、算法演示、文件读取等操作。",
)

# 不需要手动注册，@tool 装饰器已经处理
# read_py_file_tool 和 save_py_file_tool 已经在上面通过 @tool 装饰器创建


# ... existing code ...


