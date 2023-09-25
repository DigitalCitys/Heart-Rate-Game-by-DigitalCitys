# Heart Rate Game by DigitalCitys

#Creates vitals for simulated comatose person

ABNORMAL_SHIFT = 25

def plug(avg_bpm, bpm): #Plugs a comatosed patient
    return avg_bpm, bpm

def aed():
    if bpm >= avg_bpm + ABNORMAL_SHIFT or bpm <= avg_bpm - ABNORMAL_SHIFT:
        bpm = avg_bpm

def main():
    avg_bpm = input("Enter average heart rate: ")
    bpm = input("Enter current heart rate: ")
    print("Average bpm: "), avg_bpm
    print("Current bpm: "), bpm

    if bpm >= avg_bpm + ABNORMAL_SHIFT or bpm <= avg_bpm - ABNORMAL_SHIFT:
        aed_request = input("Heart rate abnormal. Administer defibrillator? YES or NO")
        if aed_request == "YES":
            aed()
        else:
            print("This could be life threatening!")

main()

if __name__ == "__main__":
    main()