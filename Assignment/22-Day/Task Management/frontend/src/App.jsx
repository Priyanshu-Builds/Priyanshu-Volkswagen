import { useState, useEffect } from 'react'
import TaskForm from './components/TaskForm'
import TaskFilters from './components/TaskFilters'
import TaskList from './components/TaskList'

const API_URL = 'http://localhost:5000'

function App() {
  const [tasks, setTasks] = useState([])
  const [priorityFilter, setPriorityFilter] = useState('')
  const [completedFilter, setCompletedFilter] = useState(false)

  const fetchTasks = async () => {
    let url = `${API_URL}/tasks?`
    if (priorityFilter) url += `priority=${priorityFilter}&`
    if (completedFilter) url += `completed=true&`

    const response = await fetch(url)
    const data = await response.json()
    setTasks(data)
  }

  useEffect(() => {
    fetchTasks()
  }, [priorityFilter, completedFilter])

  const handleToggle = async (id) => {
    await fetch(`${API_URL}/tasks/${id}`, { method: 'PUT' })
    fetchTasks()
  }

  const handleDelete = async (id) => {
    await fetch(`${API_URL}/tasks/${id}`, { method: 'DELETE' })
    fetchTasks()
  }

  return (
    <>
      <h1>Task Manager</h1>
      <TaskForm onTaskAdded={fetchTasks} />
      <TaskFilters
        priority={priorityFilter}
        completed={completedFilter}
        onPriorityChange={setPriorityFilter}
        onCompletedChange={setCompletedFilter}
      />
      <TaskList
        tasks={tasks}
        onToggle={handleToggle}
        onDelete={handleDelete}
      />
    </>
  )
}

export default App
