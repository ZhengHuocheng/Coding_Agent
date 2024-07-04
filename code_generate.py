import re

from langchain_community.llms import Ollama


llm = Ollama(model = "qwen:7b")


def extract_python_code(text: str) -> str:
    """
    提取llm回答中的Python代码, 不同LLM回答中格式可能有所不同
    """
    pattern = re.compile(r"```python\n([\s\S]*?)\n```")
    text = text
    if not re.search(pattern,text):
        pattern = re.compile(r"`py\n([\s\S]*?)\n`")
        result = re.search(pattern,text)
        result = result.group(0).strip("`").strip("py").strip()
    else:
        result = re.search(pattern,text)
        result = result.group(0).strip("```").strip("python").strip()
    return result


class Coder:
    """
    LLM生成代码类
    """
    def __init__(self):
        self.system_message = """You are helpful AI assistant.\nSolve user's tasks using your python coding and language skills.must give python code in every response."""
        self.messages = [
            {"role": "system",
             "content": f"{self.system_message}"}  
        ]  # 对话历史

    def __call__(self, query: str):
        self.messages.append(
            {"role": "user",
             "content": query}
        )  # 添加user问题

        prompt_template = """make a respondse to user based on the following messages history.\n messages history: \n {messages_history}"""
        response = llm.invoke(prompt_template.format(messages_history = self.messages))
        self.messages.append(
            {"role": "assistant",
            "content": f"{response}"}    
        )
        python_code_str = extract_python_code(response)
        return python_code_str
