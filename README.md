# web2csv
extract data from html and download as csv file


// extract data from html and download as csv file

// 2017/08/12 sivitry


[example url]

https://scholar.google.com/citations?user=jQLg-_UAAAAJ&hl=en


[Target XPath]

'//*[@id="gsc_a_b"]/tr[55]/td[1]/a'

'//*[@id="gsc_a_b"]/tr[56]/td[1]/a'


[XPath Pattern]

'//*[@id="gsc_a_b"]/tr/td[1]/a'

[Chrome Debug]

// get all paper node

x = $x('//*[@id="gsc_a_b"]/tr/td[1]/a') 


// extract paper name and concate

s = "";

for(a in x) s = s + (parseInt(a)+1) + "," + x[a].innerText+"\n";


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
