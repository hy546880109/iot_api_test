def doc_parameter(*sub):
    """写一个可以添加变量注释的装饰器"""
    def dec(obj):
       obj.__doc__ = obj.__doc__.format(*sub)
       return obj
    return dec
