from fake_useragent import UserAgent

# verify_ssl
ua = UserAgent(verify_ssl=False)
# ua.safari
# ua.ie
print(f'chrome: {ua.chrome}')
print(f'safari: {ua.safari}')
print(f'ie: {ua.ie}')
print(f'random: {ua.random}')
