

import os

def search_keywords_in_folder(folder_path, keyword):
    result = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.c', '.h')):
                file_path = os.path.join(root, file)
                matches = search_keywords_in_file(file_path, keyword)
                if matches:
                    result[file_path] = matches
    return result

def search_keywords_in_file(file_path, keyword):
    matches = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_num, line in enumerate(lines, start=1):
            if keyword in line:
                matches.append({
                    'line_num': line_num,
                    'line_content': line.strip()
                })
    return matches
if __name__ =="__main__":
    # 示例使用
    folder_path = '../../File'
    keyword = 'fu'

    result = search_keywords_in_folder(folder_path, keyword)
    total_count = sum(len(matches) for matches in result.values())

    print(f"Total keyword count: {total_count}")
    for file_path, matches in result.items():
        print(f"File: {file_path}")
        print(f"Keyword count: {len(matches)}")
        for match in matches:
            print(f"Line {match['line_num']}: {match['line_content']}")
        print("---")

