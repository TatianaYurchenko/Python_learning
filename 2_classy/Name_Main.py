
# переменная __name__ показывает откуда запущен наш скрипт
print(f'name_main: {__name__}')
def sum_test(x,y):
    return x, y
def main():
    print(1)

if __name__ == "__main__":
    main()
else:
    print(f'name_main: {__name__}')