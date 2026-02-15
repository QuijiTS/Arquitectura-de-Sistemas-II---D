import './App.css'

function App() {
  return (
    <div className="container">
      <header className="header">
        <h1>Hola, soy José Andrés Quijivix Juárez</h1>
        
        <h2>Estudiante de Ingeniería</h2>
      </header>

      <main>
        <section className="card">
          <h3>Sobre mí</h3>
          <p>
            ¡Hola! Me gusta la matematica, logica y programación. 
            Me gusta resolver problemas y aprender cosas nuevas.
          </p>
        </section>

        <section className="card">
          <h3>Mis Habilidades</h3>
          <ul className="skills-list">
            <li>C++</li>
            <li>C#</li>
            <li>Java</li>
            <li>JavaScript</li>
            <li>HTML</li>
            <li>CSS</li>
            <li>Linux</li>
            <li>MySQL</li>
          </ul>
        </section>

        <section className="card">
          <h3>Contacto</h3>
          <div className="contact-info">
            <p><strong>Email:</strong> josequijivix@umes.edu.gt</p>
            <p><strong>GitHub:</strong> github.com/QuijiTs</p>
            <p><strong>LinkedIn:</strong> linkedin.com/in/jose-quijivix</p>
          </div>
        </section>
      </main>
    </div>
  )
}

export default App