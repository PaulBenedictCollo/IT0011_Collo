date = input("Enter date (MM/DD/YY): ")

def convert_date_format(date):
    month, day, year = date.split("/")
    
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April",
        "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    
    month_name = months.get(month)
    if not month_name:
        print("Invalid month entered.")
        return
    
    year = "20" + year if len(year) == 2 else year
    
    print(f"Date Output: {month_name} {int(day)}, {year}")

convert_date_format(date)