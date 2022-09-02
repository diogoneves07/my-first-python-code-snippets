
user_text = input("\n\nOlá usuário o que você deseja salvar hoje: ")

file_path  = "./my-page.html";
handle_file = open(file_path, 'r')

current_file_lines = handle_file.readlines();
handle_file = open(file_path, 'w');

def print_message(message):
    print(f'\n\n\t{message}\n');
if ''.join(current_file_lines).count(user_text) > 0:
    print_message("Este texto já exite no arquivo!")
    exit();
    
new_file_lines = [*current_file_lines, f'\n{user_text}\n']

handle_file.writelines(new_file_lines);

print_message("Texto adicionado ao arquivo :)".rjust(20))

handle_file.close()
