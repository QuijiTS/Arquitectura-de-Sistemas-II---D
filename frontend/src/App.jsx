import { useState, useEffect } from 'react'

function App() {
  const [tasks, setTasks] = useState([])
  const [newTask, setNewTask] = useState("")

  // Cargar tareas al entrar a la página
  useEffect(() => {
    fetchTasks()
  }, [])

  const fetchTasks = async () => {
    // Se conecta a tu API en Python
    const response = await fetch("https://checklist-backend-x17t.onrender.com/tasks")
    const data = await response.json()
    setTasks(data)
  }

  const addTask = async (e) => {
    e.preventDefault()
    if (!newTask.trim()) return

    // Envía la nueva tarea al backend
    await fetch("https://checklist-backend-x17t.onrender.com/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: newTask })
    })
    setNewTask("")
    fetchTasks() // Recarga la lista para mostrar la nueva tarea
  }

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif", maxWidth: "500px", margin: "0 auto" }}>
      <h1 style={{ color: "#333" }}>Mi Checklist</h1>
      
      <form onSubmit={addTask} style={{ display: "flex", gap: "10px", marginBottom: "20px" }}>
        <input 
          type="text" 
          value={newTask} 
          onChange={(e) => setNewTask(e.target.value)} 
          placeholder="Escribe una nueva tarea..." 
          style={{ flex: 1, padding: "10px", borderRadius: "5px", border: "1px solid #ccc" }}
        />
        <button type="submit" style={{ padding: "10px 20px", background: "#007BFF", color: "white", border: "none", borderRadius: "5px", cursor: "pointer" }}>
          Agregar
        </button>
      </form>

      <ul style={{ listStyle: "none", padding: 0 }}>
        {tasks.map(task => (
          <li key={task.id} style={{ background: "#f9f9f9", margin: "10px 0", padding: "15px", borderRadius: "5px", borderLeft: "5px solid #007BFF" }}>
            {task.completed ? "✅" : "⏳"} {task.title}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App