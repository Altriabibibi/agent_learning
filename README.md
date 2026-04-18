# 🤖 Python AI Agent - 智能编程助手

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-1.2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**一个功能强大的 AI 驱动编程助手，支持代码管理、数据分析、图像处理、知识库等功能**

[功能特性](#-功能特性) • [快速开始](#-快速开始) • [使用示例](#-使用示例) • [技术栈](#-技术栈) • [文档](#-文档)

</div>

---

## 📋 项目简介

Python AI Agent 是一个基于 LangChain 框架构建的智能编程助手，能够理解自然语言指令并执行复杂的编程任务。它集成了多种实用工具，包括代码执行、文件管理、数据分析、图像处理、向量数据库等，为开发者提供全方位的辅助支持。

### ✨ 核心亮点

- 🧠 **智能对话** - 基于 DeepSeek/OpenAI 大语言模型，理解自然语言指令
- 💻 **代码管理** - 读取、分析、修改和执行 Python 代码
- 📊 **数据分析** - 自动分析 CSV/Excel 数据，生成统计报告和可视化图表
- 🖼️ **图像处理** - 支持图片调整、转换、增强、滤镜等多种操作
- 🗄️ **知识库** - 基于向量数据库的语义搜索和知识管理
- 👤 **个性化** - 自动学习用户偏好，提供定制化服务
- 📝 **文档处理** - 读取和分析 Word 文档
- 🔍 **网络搜索** - 集成 DuckDuckGo 和 Wikipedia 搜索
- 💾 **会话管理** - 保存、加载和管理对话历史

---

## 🚀 功能特性

### 1. Python 代码管理

- ✅ 读取 Python 文件（带行号显示）
- ✅ 分析和理解代码结构
- ✅ 修改和优化代码
- ✅ 执行代码并解释结果
- ✅ 代码质量分析（PEP 8 规范、复杂度等）

### 2. 数据分析与可视化

- ✅ 支持 CSV 和 Excel 文件格式
- ✅ 自动生成统计摘要（均值、标准差、缺失值等）
- ✅ 生成分布直方图
- ✅ 生成相关性热力图
- ✅ 生成分类柱状图
- ✅ 导出完整分析报告

### 3. 图像处理

- ✅ 获取图片信息（尺寸、格式、大小等）
- ✅ 调整图片尺寸（保持宽高比）
- ✅ 格式转换（JPG、PNG、WebP、BMP、GIF、TIFF）
- ✅ 图片增强（亮度、对比度、饱和度、锐度）
- ✅ 应用滤镜（模糊、锐化、灰度等）
- ✅ 裁剪和旋转图片
- ✅ 创建缩略图
- ✅ 添加文字或图片水印

### 4. 向量数据库（知识库）

- ✅ 基于 ChromaDB 的向量存储
- ✅ 语义搜索（不只是关键词匹配）
- ✅ 按主题分类管理文档
- ✅ 支持 HuggingFace 嵌入模型
- ✅ 快速检索相关知识

### 5. 用户偏好管理

- ✅ 自动学习编码风格偏好
- ✅ 记录语言偏好（中文/英文）
- ✅ 记忆工具偏好（测试框架、格式化工具等）
- ✅ 工作流程设置
- ✅ 持久化存储到 JSON 文件

### 6. 文档处理

- ✅ 读取 Word (.docx) 文档
- ✅ 提取关键信息
- ✅ 生成结构化总结

### 7. 网络信息检索

- ✅ DuckDuckGo 网页搜索
- ✅ Wikipedia 百科查询
- ✅ 隐私保护，无需 API Key

### 8. 会话管理

- ✅ 保存当前对话历史
- ✅ 加载历史会话
- ✅ 查看会话列表
- ✅ 删除过期会话
- ✅ 创建新会话
- ✅ 自动时间戳命名

---

## 🛠️ 技术栈

### 核心框架
- **LangChain** - AI Agent 框架
- **LangGraph** - 工作流引擎
- **DeepSeek/OpenAI** - 大语言模型

### 数据处理
- **Pandas** - 数据分析
- **NumPy** - 数值计算
- **Matplotlib/Seaborn/Plotly** - 数据可视化

### 图像处理
- **Pillow** - 基础图像处理
- **OpenCV** - 高级计算机视觉（可选）

### 数据库
- **ChromaDB** - 向量数据库
- **FAISS** - 相似度搜索

### 文档处理
- **python-docx** - Word 文档解析
- **Unstructured** - 通用文档框架

### 其他工具
- **DuckDuckGo Search** - 网络搜索
- **Wikipedia API** - 百科查询
- **python-dotenv** - 环境变量管理

---

## 📦 快速开始

### 环境要求

- Python 3.9+
- pip 或 conda

### 安装步骤

#### 1. 克隆项目

```bash
git clone https://gitee.com/your-username/python-ai-agent.git
cd python-ai-agent
```

#### 2. 创建虚拟环境（推荐）

```bash
# 使用 venv
python -m venv venv
.\venv\Scripts\Activate  # Windows
source venv/bin/activate  # Linux/Mac

# 或使用 conda
conda create -n agentlearn python=3.10
conda activate agentlearn
```

#### 3. 安装依赖

```bash
pip install -r requirements.txt
```

#### 4. 配置环境变量

复制 `.env.example` 为 `.env` 并填写你的 API Key：

```bash
cp .env.example .env  # Linux/Mac
copy .env.example .env  # Windows
```

编辑 `.env` 文件：

```env
DEEPSEEK_API_KEY=your-api-key-here
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEEPSEEK_MODEL=deepseek-chat
TEMPERATURE=0.7
MAX_TOKENS=1024
```

#### 5. 运行程序

```bash
python main.py
```

---

## 💡 使用示例

### 基本对话

```
你: 你好
AI: 您好！我是您的智能编程助手...

你: 现在是什么时候
AI: 现在是 2026年4月18日 19:59:05
```

### 代码管理

```
你: 帮我读取 main.py 并添加日志功能
AI: [读取文件] → [分析代码] → [添加日志] → [保存文件]

你: 运行 test.py 并解释输出
AI: [执行代码] → [分析结果] → [详细解释]
```

### 数据分析

```
你: 分析 sales_data.csv 文件
AI: 
✅ 已生成统计报告
📊 数据概览:
   - 行数: 1000
   - 列数: 8
   - 缺失值: 0
   
📈 已生成图表:
   - distribution_histogram.png
   - correlation_heatmap.png
   - category_bar_chart.png
   
📄 完整报告: analysis_output/report_2026-04-18.txt
```

### 图像处理

```
你: 查看 photo.jpg 的图片信息
AI: 
📊 图片信息:
   格式: JPEG
   尺寸: 1920 x 1080
   颜色模式: RGB
   文件大小: 2.5 MB

你: 把 image.png 转换为 JPG 格式，质量85
AI: ✅ 已转换: converted_image.jpg (压缩率: 22%)

你: 创建 photo.jpg 的缩略图，大小200px
AI: ✅ 已创建缩略图: thumbnail.png
```

### 知识库管理

```
你: 把 Python 学习资料添加到向量数据库
AI: ✅ 已添加 15 个文档到集合 "programming"

你: 搜索关于机器学习的文档
AI: 
🔍 找到 5 个相关文档:
   1. 机器学习基础概念 (相似度: 0.92)
   2. 深度学习入门教程 (相似度: 0.88)
   ...
```

### 会话管理

```
你: /menu

📋 Session 管理菜单
============================================================
1. 保存当前会话
2. 读取会话文件
3. 查看session列表
4. 删除会话文件
5. 创建新会话文件
6. 退出菜单
============================================================

请选择操作 (1-6): 1
✅ 会话已保存到: session_file/session_2026-04-18_19-59-05.txt
```

---

## 📁 项目结构

```
python-ai-agent/
├── main.py                    # 主程序入口
├── tools.py                   # 核心工具集
├── session.py                 # 会话管理模块
├── requirements.txt           # 依赖清单
├── .env                       # 环境变量配置
├── .env.example              # 环境变量模板
├── INSTALL_GUIDE.txt         # 安装指南
│
├── tools_file/               # 工具模块目录
│   ├── __init__.py
│   └── vision_tools.py       # 图像处理工具
│
├── session_file/             # 会话文件存储目录
│   └── session_*.txt
│
├── vector_db/                # 向量数据库存储
│   └── chroma_db/
│
├── analysis_output/          # 数据分析输出
│   ├── report_*.txt
│   └── *.png
│
├── agent_create_file/        # Agent 生成的文件
├── create_code_file/         # 代码生成输出
└── test_sample/              # 测试样例
```

---

## 🎯 应用场景

### 1. 开发者日常辅助
- 快速阅读和理解他人代码
- 自动化代码重构和优化
- 调试和错误分析
- 代码质量检查

### 2. 数据分析工作流
- 快速探索数据集
- 自动生成统计报告
- 可视化数据分布和相关性
- 发现数据异常和洞察

### 3. 学习和研究
- 建立个人知识库
- 语义搜索学术资料
- 整理和总结文档
- 记录学习笔记

### 4. 图像批处理
- 批量调整图片尺寸
- 格式转换和优化
- 添加水印和滤镜
- 创建缩略图

### 5. 个性化编程助手
- 记住你的编码习惯
- 适配你的工作流程
- 提供定制化建议
- 提高开发效率

---

## 📖 文档

- [安装指南](INSTALL_GUIDE.txt) - 详细的安装和问题解决
- [Skill 使用指南](SKILL_USAGE_GUIDE.md) - 如何创建和使用 Skills
- [依赖说明](requirements.txt) - 完整的依赖列表和版本要求

---

## ❓ 常见问题

### Q1: 如何获取 DeepSeek API Key？
访问 [DeepSeek 官网](https://platform.deepseek.com/) 注册并获取 API Key。

### Q2: 可以使用其他 LLM 吗？
可以！本项目支持任何兼容 OpenAI API 的服务，只需修改 `.env` 配置即可。

### Q3: Pillow 安装失败怎么办？
尝试强制重新安装：
```bash
pip install --force-reinstall --no-cache-dir Pillow==10.4.0
```

### Q4: OpenCV 是必需的吗？
不是。OpenCV 是可选依赖，用于高级图像处理。基础功能使用 Pillow 即可。

### Q5: 如何更新依赖？
```bash
pip install --upgrade -r requirements.txt
```

更多问题请查看 [INSTALL_GUIDE.txt](INSTALL_GUIDE.txt)

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [LangChain](https://github.com/langchain-ai/langchain) - 强大的 AI 应用框架
- [DeepSeek](https://deepseek.com/) - 优秀的中文大语言模型
- [ChromaDB](https://www.trychroma.com/) - 轻量级向量数据库
- 所有开源社区的贡献者

---

## 📞 联系方式

- 📧 Email: 862316710@qq.com
- 💬 Gitee Issues: [提交问题](https://gitee.com/altriadudulu/langchain_agent/issues)
- 🌐 个人主页: [你的主页链接](https://gitee.com/altriadudulu)

---

<div align="center">

**如果这个项目对你有帮助，请给个 ⭐ Star 支持一下！**

Made with ❤️ by [你的名字]

</div>
