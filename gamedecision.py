"""Game Decision"""
def main():
    """Game Decision"""
    housename = str(input())
    money = (housename == "Farmer House")*50
    money += (housename == "Commoner House")*100
    money += (housename == "Deluxe House")*500
    money += (housename == "Merchant Mansion")*15000
    money += (housename == "Nobel Fort")*35000
    result = money*16
    print(result)
main()
