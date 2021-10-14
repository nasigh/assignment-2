print("Please Enter Your Seconds :")
Seconds = int(input())
Hour = Seconds // 3600
Minute = (Seconds - 3600 * Hour) // 60
Second = (Seconds - 3600 *Hour) - 60 * Minute
print("Hour",Hour,": Minute", Minute,": Second", Second )