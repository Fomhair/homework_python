def html(items, descriptions):
    with open(f'{descriptions[0]}.html', 'w') as html_file:
        html_file.write(f'''
<!DOCTYPE html>
<html>
    <head>
        <title>{descriptions[0]}</title>
    </head>
<body>
    <div id="wrapper">
''')
        for i in range(len(items)):
            html_file.write(f'<p>{descriptions[i]}: {items[i]}</p>\n')
        html_file.write('''
    </div>
</body>
    <script>
        setInterval(function(){
           document.location.reload();
        }, 1000);
    </script>
</html>''')


def console(items, descriptions):
    for i in range(len(items)):
        print(f'{descriptions[i]}: {items[i]}')


def entry(method, items, descriptions):
    method(items, descriptions)
    return items
