items_per_line = 3; 

def show_painel(pairs_list):
    count_indexes = 0;
    while count_indexes <= len(pairs_list):  
        count_indexes+=items_per_line; 
        count_items = items_per_line;
        pairs_line = f'';
        
        while count_items>-1:
            pairs_line+=f'\t{count_indexes-count_items+1}: {pairs_list[count_indexes-count_items]}'
            count_items-=1;

        print("\n\n\t   Hello Diogo!, find all pairs!");
        print("\t\t¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨");
        print(f"{'':>10}{pairs_line}\t");
        print("\n\n\t¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n\n");
        
show_painel(["A", "B", "C", "D"]);
"""jobs_table_file_path = "./jobs-table.txt";
has_file_already_created = os.path.exists(jobs_table_file_path);

if has_file_already_created:
    jobs_table_file = open(jobs_table_file_path, 'r');
    jobs_table_content = jobs_table_file.read();
    jobs_table_lines = jobs_table_file.readlines();
    regex_username =r"(?<=\:\:)\w*(?=\:\:)";
    username = re.match(regex_username, jobs_table_content).group();
   
else:
    current_jobs = False;
    username = input('\n\n Please, insert your username: ');

    """
