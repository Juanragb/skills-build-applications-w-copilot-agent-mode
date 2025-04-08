import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://potential-robot-6695wq74969cxqq4-8000.app.github.dev/api/activities/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Activities</h1>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Type</th>
                <th>Duration (minutes)</th>
              </tr>
            </thead>
            <tbody>
              {activities.map(activity => (
                <tr key={activity._id}>
                  <td>{activity.type}</td>
                  <td>{activity.duration}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;
