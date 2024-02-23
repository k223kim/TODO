from glob import glob

todo_list = glob('../daily_todo/*.md')

if len(todo_list) >= 1:
    todo_list.sort()
    total_content = "## TODO"
    for each_todo in todo_list:
        each_content = open(each_todo, 'r').read()
        date = each_todo.replace('.md', '').split('/')[-1]
        total_content += f"\n## {date}\n{each_content}"

    with open('../README.md', 'w+') as readme:
        readme.write(total_content)

