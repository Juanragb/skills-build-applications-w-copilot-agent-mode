import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch('https://potential-robot-6695wq74969cxqq4-8000.app.github.dev/api/leaderboard/')
      .then(response => response.json())
      .then(data => setLeaderboard(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Leaderboard</h1>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Team</th>
                <th>Points</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map(entry => (
                <tr key={entry._id}>
                  <td>{entry.team}</td>
                  <td>{entry.points}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;
