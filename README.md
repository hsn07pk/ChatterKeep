# ChatterKeep System Design Documentation

## System Architecture

### High-Level Components
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Flask API     │ ──▶ │ Session Manager │ ──▶ │  SQLite Store   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Component Details

1. **API Layer** (`app.py`)
   - Handles HTTP requests and responses
   - Implements input validation
   - Routes requests to appropriate handlers
   - Manages response formatting

2. **Session Manager** (`session_manager.py`)
   - Core business logic implementation
   - Maintains in-memory session state
   - Handles conversation flow
   - Manages user context

3. **Database Layer** (`db_handler.py`)
   - Handles SQLite operations
   - Manages session persistence
   - Implements data access patterns
   - Handles connection pooling

### Data Flow
1. Request received at `/chat` endpoint
2. Request validation
3. Session lookup/creation
4. Business logic processing
5. State persistence
6. Response generation

## Database Schema

```sql
CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_phone TEXT UNIQUE NOT NULL,
    current_state TEXT NOT NULL,
    user_name TEXT,
    favorite_song TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE conversation_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER,
    message TEXT NOT NULL,
    sender TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id)
);
```


## State Machine Design
```
                ┌─────────────┐
                │   INITIAL   │
                └──────┬──────┘
                       │ hello
                       ▼
            ┌──────────────────┐
            │  AWAITING_NAME   │
            └─────────┬────────┘
                      │ name provided
                      ▼
         ┌───────────────────────┐
         │  AWAITING_SONG        │
         └───────────┬───────────┘
                     │ song provided
                     ▼
            ┌─────────────────┐
            │    COMPLETE     │
            └─────────────────┘
```

## Error Handling

1. **Input Validation**
   - Phone number format
   - Message presence
   - State transitions

2. **Database Errors**
   - Connection issues
   - Constraint violations
   - Transaction management

3. **Session Management**
   - Invalid state transitions
   - Session timeouts
   - Concurrent access

## Security Considerations

1. **Input Sanitization**
   - SQL injection prevention
   - XSS protection
   - Input length limits

2. **Rate Limiting**
   - Per-user limits
   - Global API limits
   - Burst protection

3. **Data Protection**
   - Phone number hashing
   - Sensitive data encryption
   - Session isolation

## Performance Optimizations

1. **Database**
   - Connection pooling
   - Indexed queries
   - Periodic cleanup

2. **Memory Management**
   - Session cache
   - LRU eviction
   - Memory limits

3. **Response Time**
   - Async processing
   - Request queuing
   - Load balancing

## Monitoring and Logging

1. **Application Metrics**
   - Request latency
   - Error rates
   - Session counts

2. **System Metrics**
   - CPU usage
   - Memory usage
   - Disk I/O

3. **Business Metrics**
   - Active users
   - Completion rates
   - Session duration

## Scaling Considerations

1. **Horizontal Scaling**
   - Container orchestration
   - Load balancing
   - Session stickiness

2. **Database Scaling**
   - Read replicas
   - Sharding
   - Backup strategy

3. **Cache Strategy**
   - Redis integration
   - Cache invalidation
   - Distribution
