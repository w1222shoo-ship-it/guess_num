# def inpuNumber():
#     try:
#         s = int(input('請輸入整數：'))
#     except KeyboardInterrupt:
#         print('KeyboardInterruptError')
#     except EOFError:
#         print('EOFError')
#     except ValueError:
#         print('ValueError')
#     except:
#         print('例外Exception')
#     else:
#         return s

def inpuNumber():
    s = int(input('請輸入整數：'))
    return s


while True:
    try:
        s = int(input('請輸入整數：'))
    except KeyboardInterrupt:
        print('KeyboardInterruptError')
    except EOFError:
        print('EOFError')
    except ValueError:
        print('ValueError')
    except Exception as ex:
        print('例外Exception:',ex)
    else:
        break




