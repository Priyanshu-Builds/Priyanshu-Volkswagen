import { useState } from 'react'

function TaskForm({ onTaskAdded }) {
    const [title, setTitle] = useState('')
    const [priority, setPriority] = useState('Low')

    const handleSubmit = async (e) => {
        e.preventDefault()
        if (!title.trim()) return

        const response = await fetch('http://localhost:5000/tasks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: title.trim(), priority })
        })

        if (response.ok) {
            setTitle('')
            setPriority('Low')
            onTaskAdded()
        }
    }

    return (
        <form className="task-form" onSubmit={handleSubmit}>
            <div className="form-group">
                <label>Title</label>
                <input
                    type="text"
                    placeholder="Enter task title..."
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                />
            </div>
            <div className="form-group">
                <label>Priority</label>
                <select value={priority} onChange={(e) => setPriority(e.target.value)}>
                    <option value="Low">Low</option>
                    <option value="Medium">Medium</option>
                    <option value="High">High</option>
                </select>
            </div>
            <button type="submit" className="btn-add">Add Task</button>
        </form>
    )
}

export default TaskForm
