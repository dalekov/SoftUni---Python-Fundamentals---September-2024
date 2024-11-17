title = input()
content = input()

comments = []
while True:
    comment = input()

    if comment == 'end of comments':
        print('<h1>')
        print(f'    {title}')
        print('</h1>')

        print('<article>')
        print(f'    {content}')
        print('</article>')

        for comment in comments:
            print('<div>')
            print(f'    {comment}')
            print('</div>')
        break
    # skara
    comments.append(comment)