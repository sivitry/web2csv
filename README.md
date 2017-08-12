# web2csv
extract data from html and download as csv file

Because escape characters problem, please download raw file, https://github.com/sivitry/web2csv/raw/master/README.md


// extract data from html and download as csv file

// 2017/08/12 sivitry


[example url]

https://scholar.google.com/citations?user=jQLg-_UAAAAJ&hl=en


[Target XPath]

'//*[@id="gsc_a_b"]/tr[55]/td[1]/a'

'//*[@id="gsc_a_b"]/tr[56]/td[1]/a'


//*[@id="gsc_a_b"]/tr[1]


[XPath Pattern]

'//*[@id="gsc_a_b"]/tr/td[1]/a'


[Chrome Debug]

// get all paper node

x = $x('//*[@id="gsc_a_b"]/tr') 


// extract paper name and concate

// PaperTitle:	x[a].getElementsByTagName('a')[0].innerText.replace(/\,/g,"_")

// Year: 		x[a].getElementsByTagName('td')[2].getElementsByTagName('span')[0].innerText

// ConfName: 	x[a].getElementsByTagName('div')[1].innerText.replace(/\,/g, "_")

// CitedBy:		x[a].getElementsByTagName('a')[1].innerText

s = "";

s = s+"#, PaperTitle, Year, ConfName, CitedBy \n"

for(a in x) s = s + (parseInt(a)+1) +"," 

+x[a].getElementsByTagName('a')[0].innerText.replace(/\,/g,"_") +"," 

+x[a].getElementsByTagName('td')[2].getElementsByTagName('span')[0].innerText +"," 

+x[a].getElementsByTagName('div')[1].innerText.replace(/\,/g, "_") +"," 

+x[a].getElementsByTagName('a')[1].innerText +"," 

+"\n";


// prepare http header and data to be download

csvContent = "data:text/csv;charset=utf-8,";

csvContent = csvContent+s;


// encodeURI and execute download action

var encodedUri = encodeURI(csvContent);

var link = document.createElement("a");

link.setAttribute("href", encodedUri);

link.setAttribute("download", "my_data.csv");

document.body.appendChild(link); 

link.click(); 

