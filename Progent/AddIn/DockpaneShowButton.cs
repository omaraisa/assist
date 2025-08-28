using ArcGIS.Desktop.Framework;
using ArcGIS.Desktop.Framework.Contracts;

namespace Progent
{
    internal class DockpaneShowButton : Button
    {
        protected override void OnClick()
        {
            var pane = FrameworkApplication.DockPaneManager.Find("Progent_Dockpane");
            if (pane != null)
            {
                pane.Activate();
            }
        }
    }
}
