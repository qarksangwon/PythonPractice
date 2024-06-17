from bs4 import BeautifulSoup

# HTML 문서
html_doc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <a href="https://www.example.com">Link</a>
    <div id = "main">
        <p> This is a Id selector </p>
        <p> good </p>
    </div>
  </body>
</html>
'''

# HTML 문서를 파싱하여 BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')

# 태그로 검색
title_tag = soup.title
print(title_tag)

# 클래스 명으로 검색
div_tag = soup.select('div.content')
for div in div_tag:
    print(div)

# 속성 ( 포함돼 있으면 ) 검색
a_tag = soup.find_all('a', href = True)
for a in a_tag:
    print(a)

print("----------------------------")

# Tag 객체의 요소의 이름
tag_name = title_tag.name
print(tag_name)

# Tag 객체의 요소 속성
tag_attrs = div_tag[0].attrs
print(tag_attrs)

# Tag 객체의 요소 내용
tag_content = div_tag[0].text
print(tag_content)

print("----------------------------")

# CSS 선택자 사용 요소 검색

# class 명으로
class_select = soup.select("div.content")
for div in class_select:
    print(div.text)

# id 이름으로
id_select = soup.select_one('#main').text
print(id_select)

# 자식 태그
children = soup.select('#parent > .child')

# 형제 태그
siblings = soup.select('.sibling ~ .sibling')

print("----------------------------")

# 속성 요소

# 특정 속성이 있는 모든 태그 검색
a_tags = soup.find_all('a', href=True)

# 특정 속성의 값이 포함된 요소 검색
attrs = {"class": "example", "data-id": 123}
elements = soup.find_all(attrs=attrs)

print("----------------------------")

# 부모, 자식, 형제 요소
# 부모 요소 얻기
parent_tag = title_tag.parent
print(parent_tag.name)  # 'head'

# 자식 요소 얻기
children2 = div_tag[0].children
for child in children2:
    print(child)  # <p>This is a paragraph.</p>\n<p>This is another paragraph.</p>

# 다음 형제 요소 얻기
next_sibling = title_tag.next_sibling
print(next_sibling)  # '\n'

# 이전 형제 요소 얻기
previous_sibling = title_tag.previous_sibling
print(previous_sibling)  # '\n'

print("----------------------------")

#문서 탐색

# 첫 번째 div 태그의 첫 번째 p 태그 검색
p_tag = soup.div.p

# div 태그 안에 있는 모든 p 태그 검색
p_tags = soup.div.find_all('p')

# div 태그의 부모 요소 검색
parent_tag = soup.div.parent

# 문서 전체에서 첫 번째로 나오는 p 태그 검색
first_p = soup.find('p')

# 문서 전체에서 모든 p 태그 검색
all_p = soup.find_all('p')

print("----------------------------")

# 새로운 요소 생성
new_tag = soup.new_tag('span')
new_tag.string = 'New Element'

# 기존 요소 수정
title_tag.string = 'New Title'

# 요소 추가
div_tag[0].append(new_tag)

# 속성 추가
new_tag['class'] = 'highlight'

# 요소 삭제
div_tag[0].extract()