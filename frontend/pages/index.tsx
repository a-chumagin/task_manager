import { useEffect, useState } from 'react';

interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
}

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

  useEffect(() => {
    fetch(`${apiUrl}/tasks/`)
      .then(res => res.json())
      .then(setTasks)
      .catch(console.error);
  }, [apiUrl]);

  const createTask = async () => {
    const resp = await fetch(`${apiUrl}/tasks/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, description })
    });
    if (resp.ok) {
      const task = await resp.json();
      setTasks(prev => [...prev, task]);
      setTitle('');
      setDescription('');
    }
  };

  const completeTask = async (task: Task) => {
    const resp = await fetch(`${apiUrl}/tasks/${task.id}/complete`, { method: 'PUT' });
    if (resp.ok) {
      const updated = await resp.json();
      setTasks(prev => prev.map(t => (t.id === task.id ? updated : t)));
    }
  };

  const deleteTask = async (task: Task) => {
    const resp = await fetch(`${apiUrl}/tasks/${task.id}`, { method: 'DELETE' });
    if (resp.ok) {
      setTasks(prev => prev.filter(t => t.id !== task.id));
    }
  };

  return (
    <div>
      <h1>Task Manager</h1>
      <div>
        <input
          value={title}
          onChange={e => setTitle(e.target.value)}
          placeholder="Title"
        />
        <input
          value={description}
          onChange={e => setDescription(e.target.value)}
          placeholder="Description"
        />
        <button onClick={createTask}>Add Task</button>
      </div>
      <ul>
        {tasks.map(task => (
          <li key={task.id} data-testid="task-item">
            <span style={{ textDecoration: task.completed ? 'line-through' : 'none' }}>
              {task.title}
            </span>
            <button onClick={() => completeTask(task)}>Complete</button>
            <button onClick={() => deleteTask(task)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
