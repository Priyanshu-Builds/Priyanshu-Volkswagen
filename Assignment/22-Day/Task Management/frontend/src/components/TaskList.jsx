function TaskList({ tasks, onToggle, onDelete }) {
    return (
        <div className="task-table-wrapper">
            <table className="task-table">
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Priority</th>
                        <th>Status</th>
                        <th>Created At</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {tasks.length === 0 ? (
                        <tr>
                            <td colSpan="5" className="empty-message">
                                No tasks found. Create one above!
                            </td>
                        </tr>
                    ) : (
                        tasks.map((task) => (
                            <tr key={task.id} className={task.completed ? 'completed-row' : ''}>
                                <td className="task-title">{task.title}</td>
                                <td>
                                    <span className={`priority-badge priority-${task.priority.toLowerCase()}`}>
                                        {task.priority}
                                    </span>
                                </td>
                                <td>
                                    <span className={`status-badge ${task.completed ? 'status-completed' : 'status-pending'}`}>
                                        {task.completed ? 'Completed' : 'Pending'}
                                    </span>
                                </td>
                                <td className="task-date">{task.created_at}</td>
                                <td>
                                    <div className="actions">
                                        <button className="btn-toggle" onClick={() => onToggle(task.id)}>
                                            {task.completed ? 'Undo' : 'Complete'}
                                        </button>
                                        <button className="btn-delete" onClick={() => onDelete(task.id)}>
                                            Delete
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        ))
                    )}
                </tbody>
            </table>
        </div>
    )
}

export default TaskList
