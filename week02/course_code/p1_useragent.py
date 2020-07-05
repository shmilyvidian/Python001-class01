from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
# ua.safari
# ua.ie
print(f'chrome: {ua.chrome}')
print(f'random: {ua.random}')
