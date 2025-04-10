# SimpleFlask

SimpleFlask is a lightweight Flask-based web server designed to log and monitor server activities. It provides RESTful APIs for recording and retrieving activity logs, and includes a Monitor module powered by a background service that continuously analyzes server behavior, updates monitoring data in real time, and handles monitoring-related API requests.

The Monitor runs as a separate service that calculates metrics like request rates and error frequencies, maintains the monitor database, and proactively raises alerts for abnormal patterns.

## API Endpoints

- `POST /activity`

Create a new server activity record.

**Request Body:**
```json
{
  "activity": {
    "timestamp": "2023-10-01T12:00:00Z",
    "type": "INFO",
    "message": "Server started successfully"
  }
}
```

- `GET /activity`

Retrieve all server activity records.

**Query Parameters:**

- server_id (optional): Filter by server ID.  

- `GET /monitor`

Retrieve monitoring data.

**Query Parameters:**
- server_id (optional): Filter by server ID.

## 📄 Activities Table Schema

| Field       | Type     | Description                          |
|-------------|----------|--------------------------------------|
| `id`        | Integer  | Auto-incremented unique identifier   |
| `server_id` | String   | Unique identifier for the server     |
| `type`      | Enum     | Type of activity: `'visit'` or `'login'` |
| `status`    | Enum     | Result status: `'success'` or `'error'` |
| `timestamp` | Datetime | The time the activity was recorded   |
