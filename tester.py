import numpy as np
import time

user_sea = np.full((10, 11), "🟦")
print(" 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣")
numbers_column = np.array("0,1,2,3,4,5,6,7,8,9".split(","))
user_sea[:, 0] = numbers_column
for i in user_sea:
    time.sleep(0.3)
    print("".join(i))

    ## Console version!!!