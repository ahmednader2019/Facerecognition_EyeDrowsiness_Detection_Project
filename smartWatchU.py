import webConnection as WC

# ------------------------------------
# Func  : smartWatch(status, BLoodPressure, HeartRate)
# Info  : specifes the problem with the driver using the data comming from the smart watch with the data comming from
#         the frontCamera Func. to define if the driver is only sleeping or sleeping and there are problems with him.
# Input : status --> can be defined as [sleeping, aweaking] ONLY
# Input : BLoodPressure --> Can be defined as a string like "120/80"
# Input : HeartRate --> Can be defined as intger
# retval: none
# -------------------------------------
flag = 0


def smartWatch(status, BLoodPressure, HeartRate):
    global flag
    status = status.lower()
    HR_Flag = False
    BP_Flag = False
    # status = sleeping --> check vitals
    BLoodPressureP = BLoodPressure.split("/")
    BLoodPressureU = int(BLoodPressureP[0])
    BLoodPressureD = int(BLoodPressureP[1])
    if status == "sleeping":
        # sleeping and problem with vitals
        # Children 10 years and older and adults (including seniors)	60 to 100 bpm
        if HeartRate < 60 or HeartRate > 100:
            # system activates & send massege to 911
            # print("Heart Rate Problem")
            HR_Flag = True
            # if HeartRate < 60 and HeartRate > 40:
            #     print("\"ALARM\" Sleeping")    # todo --> add  mobile function
            # if HeartRate < 40:
            #     print(f"\"DANGER\" Slow Hearted, Heart Rate = {HeartRate}")
            # if HeartRate > 100:
            #     print(f"\"DANGER\" Fast Hearted, Heart Rate = {HeartRate}")

        # sleeping and no problem with vitals
        # alarm is active
        # Check if the BLood Pressure is HIGH
        if BLoodPressureU > 135 or BLoodPressureD > 85:
            BP_Flag = True
            # if (BLoodPressureU <= 140 and BLoodPressureU > 135) or (BLoodPressureD < 90 and BLoodPressureD > 80):
            #     print(
            #         f"HIGH BLOOD PRESSURE (HYPERTENSION) STAGE 1, Blood Preassure = {BLoodPressure}")
            # elif (BLoodPressureU <= 180 and BLoodPressureU > 140) or (BLoodPressureD <= 120 and BLoodPressureD >= 90):
            #     print(
            #         f"HIGH BLOOD PRESSURE (HYPERTENSION) STAGE 2, Blood Preassure = {BLoodPressure}")
            # elif (BLoodPressureU > 180) or (BLoodPressureD > 120):
            #     print(
            #         f"HYPERTENSIVE CRISIS, Blood Preassure = {BLoodPressure}")
        # Check if the BLood Pressure is LOW
        elif BLoodPressureU < 100 or BLoodPressureD < 65:
            BP_Flag = True
            # print(
            #     f"LOW BLOOD PRESSURE (HYPOTENSION), Blood Preassure = {BLoodPressure}")

    elif status == "awake":
        if BLoodPressureU > 135 or BLoodPressureD > 85:
            # print(
            #     f"\"WARNING\" High Blood Pressure Stop and take your medicine, Blood Preassure = {BLoodPressure}")
            BP_Flag = True
        elif BLoodPressureU < 100 or BLoodPressureD < 65:
            # print(
            #     f"\"WARNING\" LOW BLOOD PRESSURE (HYPOTENSION) Stop and take your medicine, Blood Preassure = {BLoodPressure}")
            BP_Flag = True
        if HeartRate < 60 or HeartRate > 100:
            # print(
            #     f"\"WARNING\" High Heart Rate Stop and take your medicine, Heart Rate = {HeartRate}")
            HR_Flag = True

    # See which condition will activate the system
    if status == "sleeping":
        if HR_Flag == True and BP_Flag == True and flag == 0:
            print("BLood Pressure and Heart Rate Problem While Fainting")
            WC.systemActivate()
            flag = 1
            print("Calling 911")
            HR_Flag == False
            BP_Flag == False
        elif HR_Flag == True and BP_Flag == False and flag == 0:
            print("Heart Rate Problem While Fainting")
            WC.systemActivate()
            flag = 1
            print("Calling 911")
            HR_Flag == False
        elif HR_Flag == False and BP_Flag == True and flag == 0:
            print("BLood Pressure Problem While Fainting")
            WC.systemActivate()
            flag = 1
            print("Calling 911")
            BP_Flag == False
        elif HR_Flag == False and BP_Flag == False and flag == 0:
            # TODO --> Add Function to activate alarm using Mobile Phone
            print("Only Sleeping!!!!")
            WC.systemActivate()
            flag = 1

    if status == "awake":
        if HR_Flag == True and BP_Flag == True and flag == 0:
            print("BLood Pressure and Heart Rate Problem While Fainting")
            WC.systemActivate()
            flag = 1
            print("Calling 911")
            HR_Flag == False
            BP_Flag == False
        elif HR_Flag == True and BP_Flag == False and flag == 0:
            print("Heart Rate Problem While Fainting")
            WC.systemActivate()
            flag = 1
            print("Calling 911")
            HR_Flag == False
        elif HR_Flag == False and BP_Flag == True and flag == 0:
            print("BLood Pressure Problem While Fainting")
            WC.systemActivate()
            flag = 1
            print("Calling 911")
            BP_Flag == False


# while 1:
# print("-" * 80)
# smartWatch("awake", "120/80", 110)
# print("-" * 80)


# *-*-*-*-*-*- Blood Pressure *-*-*-*-*-*-*-
# Normal LESS THAN 120	and	LESS THAN 80
# ELEVATED	120 – 129	and	LESS THAN 80
# HIGH BLOOD PRESSURE (HYPERTENSION) STAGE 1	130 – 139	or	80 – 89
# HIGH BLOOD PRESSURE (HYPERTENSION) STAGE 2	140 OR HIGHER	or	90 OR HIGHER
# HYPERTENSIVE CRISIS (consult your doctor immediately)	HIGHER THAN 180	and/or	HIGHER THAN 120
# -----------------------------------------------------------------------------

# *-*-*-*-*-*- Heart Rate *-*-*-*-*-*-*-
# normal resting adult human heart rate is 60–100 bpm.
# Children 10 years and older and adults (including seniors)	60 to 100 bpm
# well-trained adult athletes 40–60
# -----------------------------------------------------------------------------
