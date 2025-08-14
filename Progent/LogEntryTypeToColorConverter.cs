using System;
using System.Globalization;
using System.Windows.Data;
using System.Windows.Media;

namespace Progent
{
    public class LogEntryTypeToColorConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is LogEntryType logType)
            {
                switch (logType)
                {
                    case LogEntryType.Error:
                        return Brushes.Red;
                    case LogEntryType.FunctionCall:
                        return Brushes.Blue;
                    case LogEntryType.FunctionResult:
                        return Brushes.Green;
                    default:
                        return Brushes.Black;
                }
            }
            return Brushes.Black;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
