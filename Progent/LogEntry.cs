using System;

namespace Progent
{
    public enum LogEntryType
    {
        Info,
        Error,
        FunctionCall,
        FunctionResult
    }

    public class LogEntry
    {
        public DateTime Timestamp { get; set; }
        public LogEntryType Type { get; set; }
        public string Message { get; set; }
        public string Details { get; set; } // For things like parameters or stack traces
    }
}
