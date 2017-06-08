# DAT
Data Analysis Tool for E///

# How to use

		python DAT.py -i -f <file> -t <table> -k <keywords> -s <sheet> [-a]
		python DAT.py -o -r <report>
		Usage: python DAT.py [OPTION]...

		Operation Mode options:
		-i                                  Import mode
		-o                                  Output mode
		-h | --help                         Print help and exit.
		
		Import options: (with '-i' option)
		-f | --file                     File to be imported
		-k | --keywords                 Keywords, the name of the column which record the hours, will be define as INT
		-t | --table                    Table to be imported to
		-s | --sheet                    Sheet Number, specify which sheet to be imported e.g: '-s 0' or '-s 1'
		-a | --init                     Whether create table, only used when the first time of import operation for each table
		
		Output options: (with '-o' option)
		-r | --report                   Templates which will be included in the report, if more than one template,use ',' to seperate. e.g: '-r 1000,1001,1002'
