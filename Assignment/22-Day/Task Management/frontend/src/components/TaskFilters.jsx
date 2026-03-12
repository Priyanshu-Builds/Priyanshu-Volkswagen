function TaskFilters({ priority, completed, onPriorityChange, onCompletedChange }) {
    return (
        <div className="filters">
            <div className="filter-group">
                <label>Priority</label>
                <select value={priority} onChange={(e) => onPriorityChange(e.target.value)}>
                    <option value="">All</option>
                    <option value="Low">Low</option>
                    <option value="Medium">Medium</option>
                    <option value="High">High</option>
                </select>
            </div>
            <div className="filter-group">
                <label className="filter-checkbox">
                    <input
                        type="checkbox"
                        checked={completed}
                        onChange={(e) => onCompletedChange(e.target.checked)}
                    />
                    <span>Completed</span>
                </label>
            </div>
        </div>
    )
}

export default TaskFilters
