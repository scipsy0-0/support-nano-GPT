from gen import make_meow, generate



def gen(start : str):
    sys = make_meow(start)


    prompt = f'''
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:

Look for answers to your questions in the documentation and don't invent anything unnecessary. 

Documentation:
{sys}

Question:
{start}

### Response
'''

    print(prompt)
    return(generate(prompt))


