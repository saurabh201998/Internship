from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title or not description:  # Check if title or description is empty
        error_message = "Title and description cannot be empty."
        return render_template('index.html', tasks=tasks, error_message=error_message)

    tasks.append({"title": title, "description": description})
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        
        if not title or not description:  # Check if title or description is empty
            error_message = "Title and description cannot be empty."
            return render_template('edit.html', index=index, task=tasks[index], error_message=error_message)
        
        tasks[index] = {"title": title, "description": description}
        return redirect(url_for('index'))
    
    return render_template('edit.html', index=index, task=tasks[index])

@app.route('/delete/<int:index>', methods=['POST'])
def delete_task(index):
    del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
