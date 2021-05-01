import GetIndexData

def main():
    Nifty_val = GetIndexData.NiftyEOD("20210101","20210110")
    print(Nifty_val)
    print(str(Nifty_val['Open']))
    
    #print(Nifty_val.info())

if __name__ == "__main__":
    main()

