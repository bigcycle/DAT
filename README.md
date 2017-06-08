# DAT
Data Analysis Tool for E///

# Packages
[MySQL-python 1.2.3](https://pypi.python.org/packages/9a/81/924d6799494cf7fb24370335c2f782088d6ac4f79e4137d4df94cea3582c/MySQL-python-1.2.3.tar.gz)

[xlwt 1.2.0](https://pypi.python.org/packages/5b/8d/22b9ec552a1d7865de39f54bd15f9db09c72a6bf8ab77b11dcce4ae336bb/xlwt-1.2.0.tar.gz#md5=1f2673a93c221f0195f342c578f04968)

[xlrd 1.0.0](https://pypi.python.org/packages/42/85/25caf967c2d496067489e0bb32df069a8361e1fd96a7e9f35408e56b3aab/xlrd-1.0.0.tar.gz#md5=9a91b688cd4945477ac28187a54f9a3b)

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
