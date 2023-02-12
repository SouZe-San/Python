
class TempConversion:
    def celsius_to_fahrenheit(celsius):
        return (celsius * (9/5)) + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * (5/9)


class CurrencyConversion :
    def inr_to_usd(inr):
        return inr / 72.5

    def inr_to_pound(inr):
        return inr * 0.00991

    def inr_to_dirham(inr):
        return inr * 0.045

    def inr_to_mark(inr):
        return inr * 0.02

    def inr_to_yen(inr):
        return inr * 1.59

    def inr_to_eur(inr):
        return inr * 0.011

class DistConversion:
    def yardToFeet(yard):
        return yard *3
    
    def milesToKm(mile):
        return mile *1.609
    
    def kmToMeter(km):
        return km /1000
    
    def meterToCentimeter(meter):
        return meter * 100
    
class Choice:
    def tempChoice():
        print("0 --> Celsius to Fahrenheit")
        print("1 --> Fahrenheit to Celsius")
        key1 =  int(input("Enter Your Choice: "))
        temp = TempConversion()
        match key1:
            case 0:
                print(">> ", temp.celsius_to_fahrenheit(int(input("Enter temp: "))))
            case 1:
                print(">> ", temp.fahrenheit_to_celsius(int(input("Enter temp: "))))
    
    def currencyChoice():
        print("0 --> To Dollar")
        print("1 --> to Pound")
        print("2 --> To Dirham")
        print("3 --> to MArk")
        print("4 --> to Yen")
        print("5 --> to Eur")
        key2 =  int(input("Enter Your Choice: "))
        curr = CurrencyConversion()
        match key2:
            case 0:
                print(">> ", curr.inr_to_usd(int(input("Enter INR: "))))
            case 1:
                print(">> ", curr.inr_to_pound(int(input("Enter INR: "))))
            case 2:
                print(">> ", curr.inr_to_dirham(int(input("Enter INR: "))))
            case 3:
                print(">> ", curr.inr_to_mark(int(input("Enter INR: "))))
            case 4:
                print(">> ", curr.inr_to_yen(int(input("Enter INR: "))))
            case 5:
                print(">> ", curr.inr_to_eur(int(input("Enter INR: "))))
    
    def distChoice():
        print("0 --> Yard to Feet")
        print("1 --> miles to Kilometer")
        print("2 --> kilometer to Meter")
        print("3 --> meter to Centimeter")
        key3 =  int(input("Enter Your Choice: "))
        dist = DistConversion()
        match key3:
            case 0:
                print(">> ", dist.yardToFeet(int(input("Enter : "))) )
            case 1:
                print(">> ", dist.milesToKm(int(input("Enter : "))) )
            case 2:
                print(">> ", dist.kmToMeter(int(input("Enter : "))) )
            case 3:
                print(">> ", dist.meterToCentimeter(int(input("Enter : "))) )

                
                
if __name__ == "__main__":
    menu = Choice()
    print("1 ---> Temperature Conversion")
    print("2 ---> Currency Conversion")
    print("3 ---> Distance Conversion")
    key = int(input("Enter Your Choice: "))
    match key:
        case 1:
            print("press 1")
            menu.tempChoice()
        case 2:
           print("Press 4")
           menu.currencyChoice()
        case 3:
            print("press 3")
            menu.distChoice()
            