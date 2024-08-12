def translatllm(text,api_url='http://127.0.0.1:8080/completion'):
    print(f'正在使用llm翻译：{text}')
    data = {
    "frequency_penalty": 0.05,
    "n_predict": 1000,
    "prompt": f"<|im_start|>system\n你是一个轻小说翻译模型，可以流畅通顺地以日本轻小说的风格将日文翻译成简体中文，并联系上下文正确使用人称代词，不擅自添加原文中没有的代词。<|im_end|>\n<|im_start|>user\n将下面的日文文本翻译成中文：{text}<|im_end|>\n<|im_start|>assistant\n",
    "repeat_penalty": 1,
    "temperature": 0.1,
    "top_k": 40,
    "top_p": 0.3
    }
    import requests
    #如果请求成功，返回翻译结果
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()
    except requests.RequestException as e:
            print(f'请求翻译API错误: {e}')
    if response.status_code >= 200 and response.status_code < 300:
        translated_text = response.json().get("content", "")
        print(f'翻译结果为：{translated_text}')
        return translated_text
    else:
        print(f'请求翻译API失败，状态码: {response.status_code}')
        return text  # 如果请求失败，返回原文
       