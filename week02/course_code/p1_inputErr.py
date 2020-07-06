import pretty_errors

class UserInputError(Exception):
    # 类进来就会执行
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorInfo = ErrorInfo

    # 类可以像字符串一样的输出
    def __str__(self):
        return self.errorInfo


userInput = 'a'

try:
    if (not userInput.isdigit()):
        # raise抛出异常
        raise UserInputError('enter wrong input')
except UserInputError as ue:
    print(ue)
finally:
    del userInput
    print('finally')
