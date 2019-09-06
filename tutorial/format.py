import json
import csv

def writeCSV(data):

    with open('formatted_data.csv', mode='w') as file:

        fieldnames = ['title', 'subtitle', 'author', 'date', 'link', 'tags', 'text']
        writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in data:
            if 'title' in row:
                title = row['title']
            else:
                title = None

            if 'subtitle' in row:
                subtitle = row['subtitle']
            else:
                subtitle = None

            if 'author' in row:
                author = row['author']
            else:
                author = None

            if 'date' in row:
                date = row['date']
            else:
                date = None

            if 'link' in row:
                link = row['link']
            else:
                link = None

            if 'tags' in row:
                tags = row['tags']
            else:
                tags = None

            if 'text' in row:
                text = row['text']
            else:
                text = None

            data = [title, subtitle, author, date, link, tags, text]
            formatted_data = []

            for input in data:
                if input is None:
                    formatted_data.append(None)
                else:
                    if isinstance(input, list):
                        formatted_list = []
                        for item in input:
                            formatted_list.append(item.encode('utf-8').strip())
                        formatted_data.append(formatted_list)
                    else:
                        unicodeText = input.encode('utf-8')
                        formattedText = unicodeText.strip()
                        formatted_data.append(formattedText)

            writer.writerow(formatted_data)

if __name__ == '__main__':
    with open('articles.json') as json_file:
        data = json.load(json_file)
        writeCSV(data)