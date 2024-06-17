from bs4 import BeautifulSoup

html = '''
<html>
    <table border=1>
        <tr>
            <td> 항목 </td>
            <td> 2013 </td>
            <td> 2014 </td>
            <td> 2015 </td>
        </tr>
        <tr>
            <td> 매출액 </td>
            <td> 100 </td>
            <td> 200 </td>
            <td> 300 </td>
        </tr>
    </table>
    <ul>
        <li> 100 </li> 
        <li> 200 </li>
    </ul> 
    <ol>
        <li> 300 </li> 
        <li> 400 </li>
    </ol>
</html>        
'''

soup = BeautifulSoup(html, 'html.parser')
# 사용 : pip install html5lib 설치 해야함
soup2 = BeautifulSoup(html, 'html5lib')
result = soup.select('td')
result2 = soup2.select('ul li')

print(result)
for val in result:
    print(val.text)

print(result2)