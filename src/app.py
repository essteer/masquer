from utils.handlers import get_response


for _ in range(10):   
    data = get_response()
    print(type(data))
    print(data)
