'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-15
FilePath: /ailearning/cases/ollama/ollama-model-cli/ollama_model_cli.py
Description: 
'''

import sys
import requests
import json

class OllamaModelManager:
    def __init__(self) -> None:
        self.basurl = 'http://localhost:11434/'
        self.headers = {"Content-Type": "application/json; charset=utf-8"}

    def commands(self):
                print('''
Larger language model ollama manager:

Usage:
    python3 ollama_model_cli.py [command]
    
Available Command:
    generate         Generate a response
    chat             Generate the next char message in a conversation between a user and an assistant
    embed            Creates vector embeddings representing the input text
    tags             Fetch a list of models and their details
    ps               Retrieve a list of models that are currently running
    show             Show more details
    create           Create a model
    copy             Copy a model
    pull             Pull a model
    push             Push a model
    delete           Delete a model
    version          Retrieve the version of the Ollama        
''')   
    
    def generate(self, *args):
        '''Generates a response for the provided prompt'''
        if len(args[0]) < 2:
            print("Usage: python3 ollama_model_cli.py generate <model> <prompt>")
            return
        model = args[0][0].lower()
        # 将模型名之后的所有参数合并为一个 prompt（支持带空格的完整问题）
        prompt = ' '.join(args[0][1:]).lower()
        print(f"Model: {model}")
        print(f"Prompt: {prompt}")
        if not model:
            print("Please provide the model your wish to use")
        elif not prompt:
            print("Please provide the prompt")
        else:
            params = {"model": model, "prompt": prompt, "stream": False}
            response = requests.post(self.basurl + 'api/generate', json=params, headers=self.headers)
            if response.status_code != 200:
                print(response.content)
            else:
                # 解析 JSON 并提取 response 字段
                result = response.json()
                print(result.get("response", "No response field in result"))
    def chat(self, *args):
        '''Generate the next chat message in a conversation between a user and an assistant.'''
        if len(args[0]) < 2:
            print("Usage: python3 ollama_model_cli.py chat <model> <prompt>")
            return
        model = args[0][0].lower()
        prompt = ' '.join(args[0][1:]).lower()
        print(f'Model: {model}')
        print(f'Prompt: {prompt}')
        if not model:
            print('Please provide the model you wish to use')
            return
        if not prompt:
            print('Please provide the prompt')
            return
        params = {'model': model, 'messages': [{"role": "user", "content": prompt}], 'stream': False}
        response = requests.post(self.basurl + "api/chat", json=params, headers=self.headers)
        if response.status_code != 200:
            print(response.content)
            return

        result = response.json()
        # 提取 message.content 字段
        message = result.get("message", {})
        print(message.get("content", "No response content in result"))

    def embed(self, *args):
        '''Creates vector embeddings representing the input text'''
        if len(args[0]) < 2:
            print("Usage: python3 ollama_model_cli.py embed <chat> <prompt>")
            return
        model = args[0][0].lower()
        prompt = ' '.join(args[0][1:]).lower()
        print(f'Model: {model}')
        print(f'Prompt: {prompt}')
        if not model:
            print("model not provide!")
            return
        if not prompt:
            print("prompt not provide!")
            return
        params = {"model": model, "input": prompt, "stream": False}
        response = requests.post(self.basurl + 'api/embed', json=params, headers=self.headers)
        if response.status_code != 200:
            print(response.content)
            return
        result = response.json()
        # 提取 embeddings
        print(result.get('embeddings', 'no response embeddings in result'))
        return

    def tags(self, *args):
        '''Fetch a list of models and their details'''
        response = requests.get(self.basurl + 'api/tags')
        if response.status_code != 200:
            print(response.content)
        else:
            result = response.json()
            formatted_json = json.dumps(result, sort_keys=True, indent=4)
            # 美化JSON数据终端输出
            print(formatted_json)
        return
    
    def ps(self, *args):
        '''Retrieve a list of models that are currently running'''
        response = requests.get(self.basurl + 'api/ps')
        if response.status_code != 200:
            print(response.content)
        else:
            result = response.json()
            formatted_json = json.dumps(result, sort_keys=True, indent=4)
            print(formatted_json)
        return

    def show(self, *args):
        '''show model details'''
        if len(args) < 1:
            print("Usage: python3 ollama_model_cli.py show <chat>")
            return
        model = args[0][0].lower()
        print(f'Model: {model}')
        if not model:
            print("not provice model")
            return
        params = {"model": model, "stream": False}
        response = requests.post(self.basurl + 'api/show', json=params, headers=self.headers)
        if response.status_code != 200:
            print(response.content)
            return
        result = response.json()
        formatted_json = json.dumps(result, sort_keys=True, indent=4)
        print(formatted_json)
        return

    def create(self, *args):
        '''create a model'''
        if len(args[0]) < 3:
            print('Usage: python3 ollama_model_cli.py create <from> <model> <system>')
            return
        from_s = args[0][0].lower()
        model = args[0][1].lower()
        system = ' '.join(args[0][2:]).lower()
        print(f'From: {from_s}')
        print(f'Model: {model}')
        print(f'System: {system}')
        if not from_s:
            print("not provide from")
            return
        if not model:
            print("not provide model")
            return
        if not system:
            print('not provide system')
            return
    
        params = {"from": from_s, "model": model, "system": system, "stream": False}
        response = requests.post(self.basurl + 'api/create', json=params, headers=self.headers)
        if response.status_code != 200:
            print(response.content)
            return
        result = response.json()
        print(result.get('status', 'no status in result'))
        return

    def copy(self, *args):
        '''copy a model'''
        if len(args[0]) < 2:
            print('Usage: python3 ollama_model_cli.py create <source> <destination>')
            return
        source = args[0][0].lower()
        destination = args[0][1].lower()
        if not source:
            print("not provide source")
            return
        if not destination:
            print("not provide destination")
            return
        params = {"source": source, "destination": destination}
        requests.post(self.basurl + "api/copy", json=params, headers=self.headers)
        return
    
    def pull(self, *args):
        '''pull a model'''
        if len(args[0]) < 1:
            print('Usage: python3 ollama_model_cli.py pull <model>')
            return
        model = args[0][0].lower()
        print(f'Model: {model}')
        if not model:
            print('not provide model')
            return
        params = {'model': model, 'stream': False}
        response = requests.post(self.basurl + 'api/pull', json=params, headers=self.headers)
        if response.status_code != 200:
            print(response.content)
            return
        result = response.json()
        # 提取 status
        print(result.get('status', 'no status content in result'))
        return

    def push(self, *args):
        '''push a model'''
        if len(args[0]) < 1:
            print('Usage: python3 ollama_model_cli.py push <model>')
            return
        model = args[0][0].lower()
        if not model:
            print('not provide model')
            return
        
        params = {"model": model, "stream": False}
        response = requests.post(self.basurl + "api/push", json=params, headers=self.headers)
        if response.status_code != 200:
            print(response.content)
            return
        result = response.json()
        status_res = result.get('status', 'no status in result')
        print(status_res)
        return

    def delete(self, *args):
        '''delete a model'''
        if len(args[0]) < 1:
            print('Usage: python3 ollama_model_cli.py delete <model>')
            return
        model = args[0][0].lower()
        print(f'Model: {model}')
        params = {'model': model}
        requests.delete(self.basurl + 'api/delete', json=params)
        return

    def version(self, *args):
        '''Retrieve the version of the Ollama'''
        response = requests.get(self.basurl + "api/version")
        if response.status_code != 200:
            print(response.content)
            return
        result = response.json()
        ver = result.get('version', 'no version in result')
        print(ver)


if __name__ == '__main__':
    manager = OllamaModelManager()
    args = sys.argv
    command_drive = {
        "generate": manager.generate, 
        "chat": manager.chat,
        "embed": manager.embed,
        "tags": manager.tags,
        "ps": manager.ps,
        "show": manager.show,
        "create": manager.create,
        "copy": manager.copy,
        "pull": manager.pull,
        "push": manager.push,
        "delete": manager.delete,
        "version": manager.version,
        }
    if len(args) < 1 :
        print("miss command arguments, please use `python3 ollama_model_cli.py`")
    elif len(args) == 1:
        manager.commands()
    else:
        cmd = args[1]
        if cmd in command_drive:
            command_drive[cmd](args[2:])
        else:
            print('unknow command, please use `python3 ollama_model_cli.py`')
