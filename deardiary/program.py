
def main():
    welcome_message()
    run_event_loop()
#    old_entries()
#    write_entry()


def welcome_message():
    print("\nwelcome to your blog, nerd\n")


def run_event_loop():
    print("what do you want to do?")
    cmd = None
    blog_data = []

    while cmd != "X":
        cmd = input("view [O]ld blogs, [W]rite a shitty new blog or e[X]it this stupid shit: ")
        cmd = cmd.lower().strip()

        if cmd == "o":
            old_entries(blog_data)
        elif cmd == "w":
            write_entry(blog_data)
        elif cmd != "x":
            print("wtf is {} supposed to do, dummy".format(cmd))
        elif cmd == "x":
            break


def old_entries(data):
    print("here's your fuckin' blogs: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx+1, entry))


def write_entry(data):
    text = input("write your fuckin shit here, press <enter> when you're done: ")
    data.append(text)


main()
