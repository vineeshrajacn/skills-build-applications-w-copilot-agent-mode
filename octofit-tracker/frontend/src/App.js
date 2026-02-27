
import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="container mt-4">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
          <img src={require('./octofitapp-small.png')} alt="OctoFit Logo" className="octofit-logo" />
          <Link className="navbar-brand text-white" to="/">OctoFit Tracker</Link>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item"><Link className="nav-link activities" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link leaderboard" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link teams" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link users" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link workouts" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </nav>
        <div className="card shadow mb-4">
          <div className="card-body">
            <Routes>
              <Route path="/activities" element={<Activities />} />
              <Route path="/leaderboard" element={<Leaderboard />} />
              <Route path="/teams" element={<Teams />} />
              <Route path="/users" element={<Users />} />
              <Route path="/workouts" element={<Workouts />} />
              <Route path="/" element={<h1 className="display-4 text-center">Welcome to OctoFit Tracker!</h1>} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
