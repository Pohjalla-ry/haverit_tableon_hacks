#!/usr/bin/env python3

def modify_file(filename):
    # The content we're looking for
    search_content = '''                    case 'select':
                    case 'mselect':

                        elem = document.createElement('select');
                        elem.setAttribute('data-key', key);
                        let option = document.createElement('option');
                        option.setAttribute('value', 0);
                        option.innerText = this.data[key]['title'];
                        elem.appendChild(option);'''

    # The replacement content
    replace_content = '''                    case 'select':
                    case 'mselect':

                        elem = document.createElement('select');
                        elem.setAttribute('data-key', key);
                        let option = document.createElement('option');
                        option.setAttribute('value', 0);
                        /**Vka Haverit */
                        if(this.data[key]['title'] == 'Kategoriat'){
                            option.innerText = "Merikorttialue";
                        }else if(this.data[key]['title'] == 'Avainsanat'){
                             option.innerText = "Paikkatieto";
                        }else{
                            option.innerText = this.data[key]['title'];
                        }                       
                        //option.innerText = this.data[key]['title'];
                        elem.appendChild(option);'''

    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the content
        new_content = content.replace(search_content, replace_content)

        # Write back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Successfully modified {filename}")

    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    modify_file('/var/www/haveritnet/wordpress/wp-content/plugins/posts-table-filterable/assets/js/filter.js')
