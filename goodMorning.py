import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
current_hour = int(time.strftime("%H", t))

if 5 <= current_hour < 12:
    print(f"Good Morning 🌅\n{current_time}")

elif 12 <= current_hour < 17:
    print(f"Good Afternoon ☀\n{current_time}")

elif 17 <= current_hour < 21:
    print(f"Good Evening 🌇\n{current_time}")

else:
    print(f"Good night 💤💤\n{current_time}")