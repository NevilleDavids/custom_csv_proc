from csvproc import CSVProcessor
csvcpu = CSVProcessor()
def print_banner():
    banner = """
 +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+
 |C|u|s|t|o|m| |C|S|V| |D|a|t|a| |T|r|a|n|s|f|o|r|m|a|t|i|o|n| |T|o|o|l|
 +-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+                                                                                                                                                 
"""
    print(banner)


def main_menu():
    print_banner()
    while True:
       
        print("1. Fetch File Path")
        print("2. Load file for Processing")
        print("3. Display Table")
        print("4. Select & Export Columns")
        print("5. Export Grouped By")
        print("6. Export Pivot Table")
        print("7. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            csvcpu.fetch_file_path()
        elif choice == "2":
            csvcpu.load_file()
        elif choice == "3":
            csvcpu.DisplayDataTabulate()
        elif choice == "4":
           csvcpu.select_columns()
        elif choice == "5":
           csvcpu.export_grouped_by()
        elif choice == "6":
           csvcpu.export_pivot_table()
        elif choice == "71":
            print("Application Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()